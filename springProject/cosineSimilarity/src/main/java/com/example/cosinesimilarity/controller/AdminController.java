package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.dto.AdminKeywordDto;
import com.example.cosinesimilarity.entity.Member;
import com.example.cosinesimilarity.service.MovieService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import javax.servlet.http.HttpSession;

@Controller
public class AdminController {

    @Autowired
    private MovieService movieService;

    @GetMapping("/admin")
    public String search(Model model, HttpSession session) {
        Member member = (Member) session.getAttribute("cosine-session-m");
        if (!member.getGrade().equals("어드민")) {
            return "redirect:/temp";
        }
        model.addAttribute("adminKeywordDto", new AdminKeywordDto());
        return "admin";
    }

    @PostMapping("/admin")
    public void search(AdminKeywordDto adminKeywordDto) {
        movieService.saveMovies(adminKeywordDto.getKeyword());
    }
}
