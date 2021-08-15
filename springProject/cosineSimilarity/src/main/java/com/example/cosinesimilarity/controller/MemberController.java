package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.dto.LoginDto;
import com.example.cosinesimilarity.dto.MemberDto;
import com.example.cosinesimilarity.entity.Member;
import com.example.cosinesimilarity.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import javax.servlet.http.HttpSession;

@Controller
public class MemberController {

    @Autowired
    private MemberService memberService;

    @GetMapping("/join")
    public String joinPage(Model model){
        model.addAttribute("memberDto", new MemberDto());
        return "join";
    }

    @PostMapping("/join")
    public String joinRequest(MemberDto memberDto) {
        memberService.saveMember(memberDto);
        return "redirect:/login";
    }

    @GetMapping("/login")
    public String loginPage(Model model) {
        model.addAttribute("loginDto", new LoginDto());
        return "login";
    }

    @PostMapping("/login")
    public String loginRequest(LoginDto loginDto, HttpSession session) {
        Member member = memberService.login(loginDto);
        session.setAttribute("cosine-session-m", member);
        return "redirect:/temp";
    }

    @GetMapping("/temp")
    public String goTemp() {
        return "temp";
    }

    @GetMapping("/logout")
    public String logoutRequest(HttpSession session) {
        session.removeAttribute("cosine-session-m");
        return "redirect:/login";
    }
}
