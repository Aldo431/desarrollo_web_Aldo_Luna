package com.tarea_4.tarea_4.models;

import java.time.LocalDateTime;
import java.util.List;

import jakarta.persistence.JoinColumn;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Column;
import jakarta.persistence.Enumerated;
import jakarta.persistence.CascadeType;
import jakarta.persistence.EnumType;


@Entity
@Table(name = "aviso_adopcion")
public class AvisoAdopcion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull
    @Column(name = "fecha_ingreso")
    private LocalDateTime fechaIngreso;

    @NotNull
    @ManyToOne
    @JoinColumn(name = "comuna_id", nullable = false)
    private Comuna comuna;

    private String sector;

    @NotNull
    private String nombre;

    @NotNull
    private String email;

    private String celular;

    @NotNull
    @Enumerated(EnumType.STRING)
    private TipoAnimal tipo;  

    @NotNull
    private Integer cantidad;

    @NotNull
    private Integer edad;

    @NotNull
    @Enumerated(EnumType.STRING)
    @Column(name = "unidad_medida")
    private UnidadEdad unidadMedida; 

    @NotNull
    @Column(name = "fecha_entrega")
    private LocalDateTime fechaEntrega;

    private String descripcion;

    @OneToMany(mappedBy = "aviso", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Foto> fotos;

    @OneToMany(mappedBy = "aviso", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<ContactarPor> contactos;

    @OneToMany(mappedBy = "aviso", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Nota> notas;

    public AvisoAdopcion() {
    }

    public AvisoAdopcion(LocalDateTime fechaIngreso,
                         Comuna comuna,
                         String sector,
                         String nombre,
                         String email,
                         String celular,
                         TipoAnimal tipo,
                         Integer cantidad,
                         Integer edad,
                         UnidadEdad unidadMedida,
                         LocalDateTime fechaEntrega,
                         String descripcion,
                         List<Foto> fotos,
                         List<ContactarPor> contactos) {

        this.fechaIngreso = fechaIngreso;
        this.comuna = comuna;
        this.sector = sector;
        this.nombre = nombre;
        this.email = email;
        this.celular = celular;
        this.tipo = tipo;
        this.cantidad = cantidad;
        this.edad = edad;
        this.unidadMedida = unidadMedida;
        this.fechaEntrega = fechaEntrega;
        this.descripcion = descripcion;
        this.fotos = fotos;
        this.contactos = contactos;
    }

    public Long getId() {
        return id;
    }

    public LocalDateTime getFechaIngreso() {
        return fechaIngreso;
    }

    public Comuna getComuna() {
        return comuna;
    }

    public String getSector() {
        return sector;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEmail() {
        return email;
    }

    public String getCelular() {
        return celular;
    }

    public TipoAnimal getTipo() {
        return tipo;
    }

    public Integer getCantidad() {
        return cantidad;
    }

    public Integer getEdad() {
        return edad;
    }

    public UnidadEdad getUnidadMedida() {
        return unidadMedida;
    }

    public LocalDateTime getFechaEntrega() {
        return fechaEntrega;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public List<Foto> getFotos() {
        return fotos;
    }

    public List<ContactarPor> getContactos() {
        return contactos;
    }
}
