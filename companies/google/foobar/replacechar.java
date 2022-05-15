
import java.util.HashMap;

class Solution {
    public static String solution(String x) {

        String a = "abcdefghijklmnopqrstuvwxyz";
        String ra = "zyxwvutsrqponmlkjihgfedcba";

        System.out.println("gtfdsg");


        HashMap<Character, Character> hash = new HashMap<>();
        for ( int i=0; i < a.length(); i++ ) {
        	hash.put(a.charAt(i), ra.charAt(i));
        }
        String s = "";
        for (char c : x.toCharArray()) {
        	Character v = hash.get(c);
        	if (v != null) {
        		s = s + hash.get(c);
        	}
        	else if (c == ' ') {
        		s = s + " ";
        	}
        	else {
        		s = s + c;
        	}
        		
        }
        System.out.println(s);

        return "cool";
    }
}

class replacechar  {
	public static void main(String[] args) {
		Solution s = new Solution();
        System.out.println("hekk");
		s.solution("kzws ov kzws ov armwztr yzm qzbvtr");
	}
}



