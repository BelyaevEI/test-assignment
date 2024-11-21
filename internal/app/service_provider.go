package app

import (
	"context"
	"log"

	"github.com/BelyaevEI/test-assignment/internal/api/auth"
	"github.com/BelyaevEI/test-assignment/internal/config"
	authRepo "github.com/BelyaevEI/test-assignment/internal/repository/auth"
	authService "github.com/BelyaevEI/test-assignment/internal/service/auth"
)

type serviceProvider struct {
	pgConfig   config.PGConfig
	grpcConfig config.GRPCConfig

	authImpl       *auth.Implementation
	authService    authService.AuthService
	authRepository authRepo.AuthRepository
}

func newServiceProvider() *serviceProvider {
	return &serviceProvider{}
}

// AuthImlp - implementation auth api layer
func (s *serviceProvider) AuthImpl(ctx context.Context) *auth.Implementation {
	if s.authImpl == nil {
		s.authImpl = auth.NewImplementation(s.AuthService(ctx))
	}

	return s.authImpl
}

// AuthService - implementation service layer
func (s *serviceProvider) AuthService(ctx context.Context) authService.AuthService {
	if s.authService == nil {
		s.authService = authService.NewService(s.AuthRepository(ctx))
	}

	return s.authService
}

// AuthRepositiry - implementation repository layer
func (s *serviceProvider) AuthRepository(ctx context.Context) authRepo.AuthRepository {
	if s.authRepository == nil {
		s.authRepository = authRepo.NewRepository(ctx)
	}

	return s.authRepository
}

// GRPCConfig reading from enviroment variables in structure
func (s *serviceProvider) GRPCConfig() config.GRPCConfig {
	if s.grpcConfig == nil {
		cfg, err := config.NewGRPCConfig()
		if err != nil {
			log.Fatalf("failed to get grpc config: %s", err.Error())
		}

		s.grpcConfig = cfg
	}

	return s.grpcConfig
}

// Read postgres config
func (s *serviceProvider) PGConfig() config.PGConfig {
	if s.pgConfig == nil {
		cfg, err := config.NewPGConfig()
		if err != nil {
			log.Fatalf("failed to get pg config: %s", err.Error())
		}

		s.pgConfig = cfg
	}

	return s.pgConfig
}
