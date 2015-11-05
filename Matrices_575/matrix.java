import java.util.*;
import java.io.*;
import java.nio.file.*;

public class matrix {
    
    public static final int N = 16;
    
    public static int add(int a, int b){
        return (a+b)%251;
    }

    public static int subtract(int a, int b) {
        return (a - b) % 251;
    }
    
    public static int multiply(int a, int b){
        return (a*b)%251;
    }

    public static int[][] random(int m, int n) {
        int[][] C = new int[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                C[i][j] = (int) (Math.random()*254+1);
        return C;
    }

    public static int[] multiply(int[][] A, int[] x) {
        int m = A.length;
        int n = A[0].length;
        if (x.length != n) throw new RuntimeException("Illegal matrix dimensions.");
        System.out.printf("m: %d \t n: %d\n", m, n);
        if (m != n) throw new RuntimeException("Illegal matrix dimensions2.");
        int[] y = new int[m];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                y[i] = add(y[i], multiply(A[i][j], x[j]));
        return y;
    }

    public static void main(String[] args) {

        System.out.println(args[0]);
        if (args[0].contains("e")) {

            byte[] resultarr = encrypt(args);
            
            try (FileOutputStream fos = new FileOutputStream("output-yeech")) {
                fos.write(resultarr);
            } catch (IOException ioe) {
                ioe.printStackTrace();
            }
        }
        else {
            // f**k programming paradime, try-catch leggo
            try {
                Path path = Paths.get("./output1");
                byte[] data = Files.readAllBytes(path);
                int[][] key = decrypt(args[1], data);
                printArr(key);
            }
            catch (Exception e) {
                System.out.println("oops?");
            }
        }
    }

    public static byte[] encrypt(String[] args) {
        int [][] key = random(N,N);
        System.out.println("KEY:");
        printArr(key);
        System.out.println("ENDKEY");
        
        String message = args[0];
        
        int[] messagebuf = new int[N];
        
        String result = "";
        byte[] resultarr = new byte[(message.length()/N+1)*N];
        
        
        for (int i=0;i<message.length();i+=N){
            for (int j=0;j<N;j++){
                if (i+j<message.length()){
                    messagebuf[j]=messagebuf[j]^(int) message.charAt(i+j); // note that they don't clear this... so it is self-encrypting
                }else{
                    messagebuf[j]=0;
                }
            }
            messagebuf = multiply(key,messagebuf);
            for (int j=0;j<N;j++){
                resultarr[i+j] = (byte) messagebuf[j];
                result += (char) messagebuf[j];
            }
        }
        System.out.println(result);
        return resultarr;
    }

    public static int[][] decrypt(String msg, byte[] encrypted) {
        //int [][] key = new int[N][N];
        //printArr(key);

        int[] messagebuf = new int[N];

        for (int i = 0 ; i < msg.length() ; i+=N) {
            byte[] current_segment = new byte[N];
            for (int j = 0 ; j < N ; j++) {
                if (i + j < msg.length()) {
                    messagebuf[j] = messagebuf[j]^(int) msg.charAt(i + j); // 'cept we really don't care lol
                }
                else {
                    messagebuf[j] = 0; // padding
                }

                current_segment[j] = encrypted[i + j];
            }

            //int[][] key = divide(current_segment, messagebuf);
            //printArr(key);
        }
        return new int[][] {{1,1,1}, {1,1,1}};
    }
    
    public static void printArr(int[][] arr){
        for (int i=0;i<arr.length;i++){
            System.out.println(Arrays.toString(arr[i]));
        }
    }
}
