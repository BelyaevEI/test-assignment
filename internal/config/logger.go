package config

import (
	"errors"
	"os"
)

const (
	logLevelEnvName = "LOGGER"
)

type LoggerConfig interface {
	Level() string
}

type loggerConfig struct {
	logLevel string
}

func NewLoggerConfig() (LoggerConfig, error) {
	logLevel := os.Getenv(logLevelEnvName)
	if len(logLevel) == 0 {
		return nil, errors.New("log level not found")
	}

	return &loggerConfig{
		logLevel: logLevel,
	}, nil
}

func (c *loggerConfig) Level() string {
	return c.logLevel
}
