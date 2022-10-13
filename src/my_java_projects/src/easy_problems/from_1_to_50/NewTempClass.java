package easy_problems.from_1_to_50;

public class NewTempClass extends TempClass{
    private String name;
    private int age;
    private String address;

    public NewTempClass() {
        System.out.println("An instance of the NewTempClass was created");
    }

    public NewTempClass(String name, int age, String address) {
        this();
        this.name = name;
        this.age = age;
        this.address = address;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public int getAge() {
        return age;
    }

    @Override
    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String getAddress() {
        return address;
    }

    @Override
    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class with name " + this.getName() + " and age " + this.getAge());
    }
}
