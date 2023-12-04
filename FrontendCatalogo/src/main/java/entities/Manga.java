
package entities;

/**
 *
 * @author NOTEBOOK
 */
public class Manga {
    
    private Long id;
    private Autor autor;
    private String titulo;
    private String genero;

    public Manga() {
    }
    public Manga(Long id, Autor autor, String titulo, String genero) {
        this.id = id;
        this.autor = autor;
        this.titulo = titulo;
        this.genero = genero;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Autor getAutor() {
        return autor;
    }

    public void setAutor(Autor autor) {
        this.autor = autor;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    @Override
    public String toString() {
        return "Manga{" + "id=" + id + ", autor=" + autor + ", titulo=" + titulo + ", genero=" + genero + '}';
    }

    
    
    
}
