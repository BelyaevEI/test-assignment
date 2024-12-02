package auth

import (
	"context"

	"github.com/BelyaevEI/test-assignment/internal/converter"
	desc "github.com/BelyaevEI/test-assignment/pkg/auth_v1"
)

func (i *Implementation) Registration(ctx context.Context, req *desc.RegistrationRequest) (*desc.Response, error) {

	token, err := i.authService.Registration(ctx, converter.ToRegistrationFromDesc(req))
	if err != nil {
		return &desc.Response{RefreshToken: ""}, err
	}

	return &desc.Response{RefreshToken: token}, nil
}
