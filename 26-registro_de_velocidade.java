public class RegistroVelocidade{

    public Double velocidadeRegistrada;
    public Double margemErro;
    
    public RegistroVelocidade(Double velocidadeRegistrada, Double margemErro){
        if (velocidadeRegistrada - margemErro > 60){
            throw new RuntimeException("O carro está acima da velocidade máxima permitida!")
        }

        else if (velocidadeRegistrada - margemErro < 6){
            throw new RuntimeException("O carro está abaixo da velocidade mínima permitida")
        }

        this.velocidadeRegistrada = velocidadeRegistrada;
        this.margemErro = margemErro;
    }

    public Double multa(){
        return velocidadeRegistrada - margemErro;

    }
}