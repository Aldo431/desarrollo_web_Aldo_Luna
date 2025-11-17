package com.tarea_4.tarea_4.models;

import java.time.LocalDateTime;


public class AvisoAdopcionDTO {

    private Long id;
    private LocalDateTime fechaIngreso;
    private String sector;
    private Integer cantidad;
    private TipoAnimal tipo;
    private Integer edad;
    private UnidadEdad unidadMedida;
    private String comunaNombre;
    private Double notaPromedio; 

    public AvisoAdopcionDTO() {}

    public AvisoAdopcionDTO(Long id,
                             LocalDateTime fechaIngreso,
                             String sector,
                             Integer cantidad,
                             TipoAnimal tipo,
                             Integer edad,
                             UnidadEdad unidadMedida,
                             String comunaNombre,
                             Double notaPromedio) {
        this.id = id;
        this.fechaIngreso = fechaIngreso;
        this.sector = sector;
        this.cantidad = cantidad;
        this.tipo = tipo;
        this.edad = edad;
        this.unidadMedida = unidadMedida;
        this.comunaNombre = comunaNombre;
        this.notaPromedio = notaPromedio;
    }

    public Long getId() {
        return id;
    }

    public LocalDateTime getFechaIngreso() {
        return fechaIngreso;
    }

    public String getSector() {
        return sector;
    }

    public Integer getCantidad() {
        return cantidad;
    }

    public TipoAnimal getTipo() {
        return tipo;
    }

    public Integer getEdad() {
        return edad;
    }

    public UnidadEdad getUnidadMedida() {
        return unidadMedida;
    }

    public String getComunaNombre() {
        return comunaNombre;
    }

    public Double getNotaPromedio() {
        return notaPromedio;
    }
}