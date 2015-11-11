/*
e = 2065659454658019741780522570419376267931036082571377113532943424886952853219885592888546058433700094658894057336807857079282524074810812659298259543680548665395629065595040507999387715499956304724045136225056327421882545091174374570023424535112498454573479876181424784110131185483172182567718771705357890630390524098272037132047386754987122041548608712507049648368618233039815189112679401751673818053814414216405396571717867682135903220899506431110321
N = 15400885188485388049229946115512511353845197043097285530075409718388590971501843031369538958459169822303236190066396248608622037606343820483841010751744253075387229800570159335032337643532517901246837393402971049197240224798725537792741680433188129746634857065058382842170932826771717848138506068088433052708419697033705085891848264001733184025953542048382911813415973137050911264369215530304400136356189146873204291644040454522340419405810227455030169
c = 760894689262844885371751591201448779521835108353743313800590228287883246832521161155713798220976743626366322709974313368781948082191281660975308519380232531497704568353066256030126511723916722931253492903191292586450258770582815239107520640326529085182608791895866376091631630442008101620467535339697524745040884971556649638477516510814746222381658518518495136569791463216844279744897839803187178714271885199986261696934285363856834444143640949914211
blargh    = 22283534875599850876789018475081041841486283168431437253694779271474493250718084374708805570320871577840506514946714255341522174551232145987973981725106628322276753455869316082736457510457896929067465122706520430218823951936056833405155924829171597626126375168082041045894081707614593844823516533002772287670178875345325730980927465940712521614480113783316038427900701982536598794663064488757402428327200828206192106573612266819121374764704827640993563
*/


import java.math.BigInteger;
import java.security.SecureRandom;

public class RSA {
   private final static BigInteger one      = new BigInteger("1");
   private final static SecureRandom random = new SecureRandom();

   private BigInteger privateKey;
   private BigInteger publicKey;
   private BigInteger modulus;
   
   private BigInteger p;
   private BigInteger q;
   private BigInteger r;

   RSA(int N) {
      p = BigInteger.probablePrime(N/3, random);
      q = BigInteger.probablePrime(N/3, random);
      r = BigInteger.probablePrime(N/3, random);
      BigInteger phi = (p.subtract(one)).multiply(q.subtract(one)).multiply(r.subtract(one));
      //phi = (p-1) * (q-1) * (r-1)

      modulus    = p.multiply(q).multiply(r); //p*q*r = N
      privateKey  = BigInteger.probablePrime(N/7-5, random); //d
      publicKey = privateKey.modInverse(phi); //e
   }


   BigInteger encrypt(BigInteger message) {
      return message.modPow(publicKey, modulus); //pow(m,e,N)
   }

   BigInteger decrypt(BigInteger encrypted) {
      return encrypted.modPow(privateKey, modulus); //pow(c,d,N)
   }

   public String toString() {
      String s = "";
      s += "public  = " + publicKey  + "\n";
      s += "private = " + privateKey + "\n";
      s += "modulus = " + modulus;
      return s;
   }

   public static void main(String[] args) {
      int N = Integer.parseInt(args[0]);
      RSA key = new RSA(N);
      System.out.println(key);

      String s = "AAAAA";
      byte[] bytes = s.getBytes();
      BigInteger meowwww = key.p.multiply(key.q).add(key.q.multiply(key.r)).add(key.p.multiply(key.r)); //p*q + q*r + p*r
      BigInteger x = BigInteger.probablePrime(N, random);
      BigInteger message = (new BigInteger(bytes)).multiply(meowwww.subtract(key.p.add(key.q.add(key.r)))).xor(x);
      // M(pq + qr + pr - (p+q+r)) ^ x

      BigInteger encrypt = key.encrypt(message);
      BigInteger decrypt = key.decrypt(encrypt);
      BigInteger orig = decrypt.xor(x).divide(meowwww.subtract(key.p.add(key.q.add(key.r))));
      System.out.println("encrypted = " + encrypt);
      System.out.println("blargh    = " + x);

      System.out.println("message   = " + message);
      System.out.println("decrypted = " + decrypt);
      System.out.println("bytes     = " + new BigInteger(bytes));
      System.out.println("xord      = " + orig);
      System.out.println("pls       = " + new String(orig.toByteArray()));
   }
}
