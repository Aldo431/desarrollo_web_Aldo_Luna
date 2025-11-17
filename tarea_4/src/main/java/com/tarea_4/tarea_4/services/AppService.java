package com.tarea_4.tarea_4.services;

import com.tarea_4.tarea_4.models.AvisoRepository;
import com.tarea_4.tarea_4.models.Nota;
import com.tarea_4.tarea_4.models.NotaRepository;
import com.tarea_4.tarea_4.models.AvisoAdopcion;
import com.tarea_4.tarea_4.models.AvisoAdopcionDTO;

import java.util.List;
import org.springframework.stereotype.Service;
import java.util.Objects;

@Service
public class AppService {

    private final AvisoRepository avisoRepository;
    private final NotaRepository notaRepository;

    public AppService(AvisoRepository avisoRepository, NotaRepository notaRepository) {
        this.avisoRepository = avisoRepository;
        this.notaRepository = notaRepository;
    }

    public List<AvisoAdopcionDTO> getAvisosDTO() {
        return avisoRepository.findAvisosDTO();
    }
    public void guardarEvaluacion(Long avisoId, int notaValor) {

        AvisoAdopcion aviso = avisoRepository.findById(Objects.requireNonNull(avisoId))
                .orElseThrow(() -> new RuntimeException("Aviso no encontrado"));

        Nota nota = new Nota(notaValor, aviso);

        notaRepository.save(nota);
    }
}