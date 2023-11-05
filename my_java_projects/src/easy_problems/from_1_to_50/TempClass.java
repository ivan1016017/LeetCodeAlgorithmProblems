package easy_problems.from_1_to_50;

public class TempClass {
    private String name;
    private int age;
    private String address;

    public TempClass() {
        System.out.println("This is an instance of the Temp Class");
    }

    public TempClass(String name, int age, String address) {
        this();
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void returnNumbers(){

    }
}
