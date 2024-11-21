package auth

import "context"

// AuthRepository represents a repository for auth entities.
type AuthRepository interface{}

type repo struct {
}

func NewRepository(ctx context.Context) AuthRepository {
	return &repo{}
}
