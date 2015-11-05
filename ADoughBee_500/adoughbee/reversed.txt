int RegisterSoftware(HWND h, unsigned int message, unsigned int wParam, int iParam)
{
    if message == 272:
        return 1
    if message != 273:
        return 0
    if wParam == 2:
        return 1
    if wParam == 1:
        char email[64]; //on heap
        //get input
        char serial[26]; //on heap
        //get input
        if strlen(serial) != 25:
            show "Serial must be 25 chars long"
            return 0
         x = 4919
         for (i=0;; ++i)
         {
            if i > strlen(email): break
            x ^= email[i]
         }
         //x = 4946 at this point
        y = -559023599
        for grp in every group of 5: //split 25 into 5 groups of 5
            grp = toupper(grp)
            num = frombase36(grp)
            y ^= x * num
            
        result = y ^ x
        if result == -86730271:
            Win //<----WE WANT THIS
        else:
            Fail
}
