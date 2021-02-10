
import java.util.Arrays;
import java.util.Comparator;
import java.util.Collections;

class Solution {
    public static int solution(String n, int b) {
        char CA[] = n.toCharArray();
        Collections.sort(CA);
        char A1[] = CA;
        Collections.reverse(CA);
        char A2[] = CA;
        System.out.println(new String(CA));
        System.out.println(new String(RA));
        int numb = Integer.parseInt(new String(A1)) - Integer.parseInt(new String(A2));
        return numb;
    }
}

class loop  {
	public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(s.solution("210022", 3));
	}
}



