import java.util.ArrayList;

public class dynamicarray{
    public static ArrayList<String> merge(String[] words, String[] more){
        ArrayList<String> sentence = new ArrayList<String>();
        for (String w: words) sentence.add(w);
        for (String w: more) sentence.add(w);
        return sentence;

    }
    public static void main(String[] args) {
        System.out.println("In Main");

        String[] str1 = {"I can't give up", "የኢትዮጵያ ፌዴራላዊ ዴሞክራሲ"};
        String[] str2 = {"I have come too far"};

        ArrayList<String> res = new ArrayList<String>();
        res = merge(str1,str2);

        System.out.println(res);
    }
}
