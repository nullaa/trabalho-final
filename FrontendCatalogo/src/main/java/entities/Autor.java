
package entities;

/**
 *
 * @author NOTEBOOK
 */
public class Autor {
    
    private Long id;
    private String nome;
    private String datanasc;
    private String idade;

    public Autor() {
    }
    public Autor(Long id, String nome, String datanasc,String idade ) {
        this.id = id;
        this.nome = nome;
        this.datanasc = datanasc;
        this.idade= idade;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDatanasc() {
        return datanasc;
    }

    public void setDatanasc(String datanasc) {
        this.datanasc = datanasc;
    }

    public String getIdade() {
        return idade;
    }

    public void setIdade(String idade) {
        this.idade = idade;
    }

    @Override
    public String toString() {
        return nome;
    }
    
    
    
    
}
