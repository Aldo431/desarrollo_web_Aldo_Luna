package com.tarea_4.tarea_4.models;

import jakarta.persistence.*;

@Entity
@Table(name = "foto")
public class Foto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String rutaArchivo;
    private String nombreArchivo;

    @ManyToOne
    @JoinColumn(name = "aviso_id", nullable = false)
    private AvisoAdopcion aviso;

    public Foto() {}

    public Foto(String rutaArchivo, String nombreArchivo, AvisoAdopcion aviso) {
        this.rutaArchivo = rutaArchivo;
        this.nombreArchivo = nombreArchivo;
        this.aviso = aviso;
    }

    public Long getId() { return id; }
    public String getRutaArchivo() { return rutaArchivo; }
    public String getNombreArchivo() { return nombreArchivo; }
    public AvisoAdopcion getAviso() { return aviso; }
}
