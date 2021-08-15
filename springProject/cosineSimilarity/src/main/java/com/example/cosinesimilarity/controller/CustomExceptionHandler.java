package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.dto.MemberDto;
import com.example.cosinesimilarity.exception.CustomJoinException;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class CustomExceptionHandler {

    @ExceptionHandler({CustomJoinException.class})
    public String CustomJoinException(CustomJoinException e, Model model) {
        model.addAttribute("memberDto", new MemberDto());
        model.addAttribute("errorMessage", e.getMessage());
        return "join";
    }
}
