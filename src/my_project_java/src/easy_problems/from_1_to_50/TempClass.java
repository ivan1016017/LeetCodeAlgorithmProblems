package easy_problems.from_1_to_50;

public class TempClass extends LongestCommonPrefix{

    private String name;
    private String address;
    private int age;

    public TempClass(String name, String address, int age) {
        this.name = name;
        this.address = address;
        this.age = age;
    }

    public TempClass() {
        System.out.println("An instance of the class was created");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the class with name: " + this.getName() + " and age: " + this.getAge() + " and address: " +  this.getAddress());
    }
}
