package com.tarea_4.tarea_4.models;

import jakarta.persistence.*;

@Entity
@Table(name = "contactar_por")
public class ContactarPor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    public enum Medio {
        whatsapp, telegram, X, instagram, tiktok, otra
    }

    @Enumerated(EnumType.STRING)
    private Medio nombre;

    private String identificador;

    @ManyToOne
    @JoinColumn(name = "actividad_id", nullable = false)
    private AvisoAdopcion aviso;

    public ContactarPor() {}

    public ContactarPor(Medio nombre, String identificador, AvisoAdopcion aviso) {
        this.nombre = nombre;
        this.identificador = identificador;
        this.aviso = aviso;
    }

    public Long getId() { return id; }
    public Medio getNombre() { return nombre; }
    public String getIdentificador() { return identificador; }
    public AvisoAdopcion getAviso() { return aviso; }
}
