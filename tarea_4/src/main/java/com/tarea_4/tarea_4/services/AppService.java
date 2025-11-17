package com.tarea_4.tarea_4.services;

import com.tarea_4.tarea_4.models.AvisoRepository;
import com.tarea_4.tarea_4.models.AvisoAdopcionDTO;

import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class AppService {

    private final AvisoRepository avisoRepository;

    public AppService(AvisoRepository avisoRepository) {
        this.avisoRepository = avisoRepository;
    }

    public List<AvisoAdopcionDTO> getAvisosDTO() {
        return avisoRepository.findAvisosDTO();
    }
}
