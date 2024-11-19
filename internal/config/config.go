package config

import "github.com/joho/godotenv"

// Load config file to enviroment variables
func Load(path string) error {
	err := godotenv.Load(path)
	if err != nil {
		return err
	}

	return nil
}
