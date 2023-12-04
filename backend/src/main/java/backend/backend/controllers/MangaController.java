package backend.backend.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import backend.backend.entities.Manga;
import backend.backend.repositores.MangaRepository;
import lombok.AllArgsConstructor;

@RestController
@AllArgsConstructor

public class MangaController {
    MangaRepository repos;

    @GetMapping("/mangas")
    public List<Manga> getAllAutor() {
        return repos.findAll();
    }
    @GetMapping("/autor/{id}")
    public Manga geAutorById(@PathVariable Long id){
        return repos.findById(id).get();
    }

    @PostMapping("manga")
    public Manga savemManga(@RequestBody Manga manga){
        return repos.save(manga);
    }
    @DeleteMapping("/manga{id}")
    public void deleteManga(@PathVariable Long id){
        repos.deleteById(id);
    }

    
    
}
