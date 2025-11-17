package com.tarea_4.tarea_4.controllers;

import com.tarea_4.tarea_4.services.AppService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;


@Controller
public class AppController {

    private final AppService appService;

    public AppController(AppService appService) {
        this.appService = appService;
    }

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("avisos", appService.getAvisosDTO());
        return "index";
    }
}