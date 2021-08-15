package com.example.cosinesimilarity.repository;

import com.example.cosinesimilarity.entity.Movie;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MovieRepository extends JpaRepository<Movie, Long> {
}
