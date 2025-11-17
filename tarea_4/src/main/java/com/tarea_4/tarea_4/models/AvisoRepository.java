package com.tarea_4.tarea_4.models;

import java.util.List;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AvisoRepository extends JpaRepository<AvisoAdopcion, Long> {

    @Query("""
        SELECT new com.tarea_4.tarea_4.models.AvisoAdopcionDTO(
        a.id, a.fechaIngreso, a.sector, a.cantidad,
        a.tipo, a.edad, a.unidadMedida,
        c.nombre,
        COALESCE(AVG(n.nota), 0)
        )
        FROM AvisoAdopcion a
        JOIN a.comuna c
        LEFT JOIN a.notas n
        GROUP BY a.id, a.fechaIngreso, a.sector, a.cantidad,
                a.tipo, a.edad, a.unidadMedida, c.nombre
        ORDER BY a.fechaIngreso DESC
    """)
    List<AvisoAdopcionDTO> findAvisosDTO();
}