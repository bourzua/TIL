package beans;

import java.util.ArrayList;
import java.util.List;

public class sdf {
	
public static void main(String[] args) {
	
	List<List<String>> a = new ArrayList<List<String>>();
	
	List<String> b = new ArrayList<String>();
	b.add("Á¦¹ß");
	b.add("Á»");
	
	a.add(b);
	
	System.out.println(a.get(0).get(0));
}

}
