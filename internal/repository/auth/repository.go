package auth

import (
	"context"
	"database/sql"
	"log"

	"github.com/BelyaevEI/test-assignment/internal/storage/postgre"
)

// AuthRepository represents a repository for auth entities.
type AuthRepository interface{}

type repo struct {
	db *sql.DB
}

func NewRepository(ctx context.Context, dsn string) AuthRepository {
	pg, err := postgre.New(ctx, dsn)
	if err != nil {
		log.Fatalf("failed connet to database: %s", err.Error())
	}

	return &repo{db: pg}
}
