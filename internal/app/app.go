package app

import (
	"context"
	"flag"
	"log"
	"net"
	"os"
	"os/signal"
	"sync"
	"syscall"

	"github.com/BelyaevEI/platform_common/pkg/closer"

	"google.golang.org/grpc"
)

var configPath string

func init() {
	configPath = os.Getenv("CONFIG_PATH")
	flag.Parse()
}

// App represents the app
type App struct {
	serviceProvider *serviceProvider
	grpcServer      *grpc.Server
}

// NewApp creates and initializate a new app.
func NewApp(ctx context.Context) (*App, error) {
	a := &App{}

	err := a.initDependens(ctx)
	if err != nil {
		return nil, err
	}

	return a, nil
}

// Run application
func (a *App) Run(ctx context.Context) error {

	defer func() {
		closer.CloseAll()
		closer.Wait()
	}()

	ctx, cancel := context.WithCancel(ctx)

	wg := &sync.WaitGroup{}
	wg.Add(1)

	go func() {
		defer wg.Done()

		err := a.runGRPCServer()
		if err != nil {
			log.Fatalf("failed to run grpc server: %v", err)
		}

	}()

	gracefulShutdown(ctx, cancel, wg)
	return nil
}

func gracefulShutdown(ctx context.Context, cancel context.CancelFunc, wg *sync.WaitGroup) {

	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)

	select {
	case <-ctx.Done():
		log.Println("terminating: context cancelled")
	case <-sig:
		log.Println("terminating: via signal")
	}

	cancel()
	if wg != nil {
		wg.Wait()
	}
}

// Start listen grpc server
func (a *App) runGRPCServer() error {
	log.Printf("GRPC server is running on %s", a.serviceProvider.GRPCConfig().Addres())

	list, err := net.Listen("tcp", a.serviceProvider.GRPCConfig().Addres())
	if err != nil {
		return err
	}

	err = a.grpcServer.Serve(list)
	if err != nil {
		return err
	}

	return nil
}
