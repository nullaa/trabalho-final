package backend.backend.repositores;

import org.springframework.data.jpa.repository.JpaRepository;


import backend.backend.entities.Autor;

public interface AutorRepository  extends JpaRepository<Autor,Long> {
    
}
