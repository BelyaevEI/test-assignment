package auth

import (
	"context"

	"github.com/BelyaevEI/test-assignment/internal/model"
)

func (s *serv) Login(ctx context.Context, login *model.UserLogin) (string, error) {
	return "", nil
}