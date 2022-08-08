import java.io.Serial;
import java.io.Serializable;

public class ProductOnline implements Serializable{
    private String name;
    private Double price;
    private static final long serialVersionUID = 1l;

    public ProductOnline(){}

    public ProductOnline(String name, Double price){
        this.price = price;
        this.name = name;

    }

}