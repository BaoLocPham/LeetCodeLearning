class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        // Approach 1: using HashSet
        // Time O(n^2)
        // Space O(n)
        Set visited = new HashSet(), repeated = new HashSet();
        for (int i=0; i+9<s.length(); i++){
            String sub = s.substring(i, i+10);
            if (!visited.add(sub))
                repeated.add(sub);
        }
        return new ArrayList(repeated);

        // Apprach 2: rolling-hash
        // Time O(n)
        // Space O(n)
        Set<Integer> words = new HashSet<>();
        Set<Integer> doubleWords = new HashSet<>();
        List<String> rs = new ArrayList<>();
        char[] map = new char[26];
        map['A' - 'A'] = 0;
        map['C' - 'A'] = 1;
        map['G' - 'A'] = 2;
        map['T' - 'A'] = 3;
        for (int i=0; i<s.length()-9; i++){
            int v= 0;
            for (int j=i; j<i+10; j++){
                v<<=2;
                v+=map[s.charAt(j)-'A'];
            }
            if (!words.add(v) && doubleWords.add(v)){
                rs.add(s.substring(i, i+10));
            }
        }
        return rs;
    }
}