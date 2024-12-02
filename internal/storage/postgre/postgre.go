package postgre

import (
	"context"
	"database/sql"
)

func New(ctx context.Context, dsn string) (*sql.DB, error) {
	pg, err := sql.Open("pgx", dsn)
	if err != nil {
		return nil, err
	}

	err = pg.Ping()
	if err != nil {
		return nil, err
	}

	return pg, nil
}
