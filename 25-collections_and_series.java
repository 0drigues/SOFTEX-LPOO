import java.io.Serializable;
import java.io.Serial;

public class Main {

    public static void main(String[] args) throws IOException, ClassNotFoudException{
        ProductOnline producOnline = new ProductOnline(name: "carro", price = 70000d);
        System.out.println(producOnline)

        ObjectOutputStream objectOutput = new ObjectOutputStream(new FileOutputStream(name: "carro.bytej"));
        objectOutput.writeObject(producOnline);
        objectOutput.close();

        ObjectInputStream objectInput = new ObjectInputStream(new FileInputStram(name: "carro.bytej"))
        ProductOnline producOnline = (ProductOnline) objectInput.readObject();
        objectInput.close();
        System.out.println(producOnline.getName());
        

    
    
    
    
    
    
    
    
    }
}