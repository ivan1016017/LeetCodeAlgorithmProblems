package easy_problems.from_1_to_50;

public class NewTempClass extends TempClass{
    private String name;
    private int age;
    private String address;

    public NewTempClass() {
        System.out.println("An instance of the class NewTempClass was created.");
    }

    public NewTempClass(String name, int age, String address) {
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

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the NewTempClass with name " + this.getName() + " and age " + this.getAge());
    }
}
