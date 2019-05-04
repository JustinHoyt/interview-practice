import java.util.HashMap;

public class JavaExample {
  public static void main(String[] args) {
    // initialize map
    HashMap<String, String> myMap = new HashMap<String, String>();

    // add items
    myMap.put("name", "Jack");
    myMap.put("age", "26");
    myMap.put("address", "Downtown");
    myMap.put("age", "27");

    // check if key is in map
    if (myMap.containsKey("age"))
        System.out.println(myMap.get("age"));

    // iterate over map
    for (String key : myMap.keySet()) {
      System.out.println("{" + key + ": " + myMap.get(key) + "}");
    }
  }
}
