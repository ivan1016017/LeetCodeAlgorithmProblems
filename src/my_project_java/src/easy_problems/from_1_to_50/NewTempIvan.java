package easy_problems.from_1_to_50;

public class NewTempIvan extends TempClass{

    private String name;
    private String address;
    private int age;

    public NewTempIvan() {
        System.out.println("An instance of the class NewTempIvan was called");
    }

    public NewTempIvan(String name, String address, int age) {
        this();
        this.name = name;
        this.address = address;
        this.age = age;
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
        System.out.println("This is an instance of the class with name " + this.getName());
    }
}
