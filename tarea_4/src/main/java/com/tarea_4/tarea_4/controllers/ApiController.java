package com.tarea_4.tarea_4.controllers;

import com.tarea_4.tarea_4.models.AvisoAdopcionDTO;
import com.tarea_4.tarea_4.services.AppService;
import com.tarea_4.tarea_4.models.EvaluacionRequest;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;  
import java.util.List;


@RestController
@RequestMapping("/api")
public class ApiController {

    private final AppService appService;

    public ApiController(AppService appService) {
        this.appService = appService;
    }

    @GetMapping("/avisos")
    public List<AvisoAdopcionDTO> listarAvisos() {
        return appService.getAvisosDTO();
    }
    @PostMapping("/avisos/{id}/evaluar")
    
    public ResponseEntity<Void> evaluarAviso(
            @PathVariable Long id,
            @RequestBody EvaluacionRequest request) {

        appService.guardarEvaluacion(id, request.getNota());
        return ResponseEntity.ok().build();
    }
}
