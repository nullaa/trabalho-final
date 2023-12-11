package backend.backend.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.RestController;

import backend.backend.entities.Autor;
import backend.backend.repositores.AutorRepository;
import lombok.AllArgsConstructor;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@AllArgsConstructor

public class AutorController {
    AutorRepository repos;

    @GetMapping("/autores")
    public List<Autor> getAllAutor() {
        return repos.findAll();
    }
    @GetMapping("/autor/{id}")
    public Autor geAutorById(@PathVariable Long id){
        return repos.findById(id).get();
    }

    @PostMapping("/autor")
    public Autor saveAutor(@RequestBody Autor autor){
        return repos.save(autor);
    }
    @DeleteMapping("/autor/{id}")
    public void deleteAutor(@PathVariable Long id){
        repos.deleteById(id);
    }

    
    
}
