package easy_problems.from_1_to_50;

public class TempIvanClass extends TempClass {

    private String name;
    private int age;
    private String address;

    public TempIvanClass(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public TempIvanClass() {
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

    @Override
    public void returnNumbers() {
        System.out.println("The age of " + this.getName() + " is " + this.getAge());
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
