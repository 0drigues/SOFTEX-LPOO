public class Multas{
    public static void main(String[] args){

        Double velocidadeRegistrada = 100 //pode variar
        Double margemErro = velocidadeRegistrada * 0.2 //pode variar

        try{
            RegistroVelocidade v = new RegistroVelocidade(velocidadeRegistrada, margemErro);
            System.out.println(v.multa)
        }

        catch (RuntimeException erro){
            System.out.println(erro.getMessage());
        }
    }
}