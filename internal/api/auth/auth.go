package auth

import (
	desc "github.com/BelyaevEI/test-assignment/pkg/auth_v1"
)

type Implementation struct {
	desc.UnimplementedAuthV1Server
}

// NewImplementation creates a new auth API implementation.
func NewImplementation() *Implementation {
	return &Implementation{}
}
