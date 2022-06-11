package easy_problems.from_1_to_50;

import java.util.ArrayList;

public class GroceryList {

    private ArrayList<String> groceryList = new ArrayList<String>();

    public void addGroceyItem(String item) {
        groceryList.add(item);
    }

    public void printGroceryList() {
        System.out.println("You have " + groceryList.size() + " items.");
        for (int i = 0; i < groceryList.size(); i++){
            System.out.println((i+1) + ". " + groceryList.get(i));
        }
    }

    public void modigyGroceryItem(int position, String newItem){
        groceryList.set(position,newItem);
        System.out.println("Grocery item number " + position + " has been updated to " + newItem);
    }

    public void removeGroceryItem(int position){
        groceryList.remove(position);
    }
}
