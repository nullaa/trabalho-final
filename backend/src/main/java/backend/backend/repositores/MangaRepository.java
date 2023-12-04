package backend.backend.repositores;

import org.springframework.data.jpa.repository.JpaRepository;


import backend.backend.entities.Manga;

public interface MangaRepository  extends JpaRepository<Manga,Long> {
    
}
