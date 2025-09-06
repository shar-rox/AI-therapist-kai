# Overview

This is a therapeutic AI chat application that provides mental health support through real-time conversations. The system combines a React frontend with an Express.js backend to create an empathetic AI companion that can detect crisis situations and provide appropriate resources. The application uses WebSocket connections for real-time messaging and integrates with OpenAI's API to generate therapeutic responses.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: React with TypeScript using Vite as the build tool
- **UI Library**: Radix UI components with Tailwind CSS for styling
- **State Management**: TanStack Query for server state management and local React state for UI state
- **Routing**: Wouter for lightweight client-side routing
- **Real-time Communication**: WebSocket client for bidirectional communication with the server

## Backend Architecture
- **Framework**: Express.js with TypeScript
- **Database ORM**: Drizzle ORM configured for PostgreSQL
- **Real-time Communication**: WebSocket server using the 'ws' library for chat functionality
- **Session Management**: In-memory storage implementation with interface for future database integration
- **Error Handling**: Centralized error middleware for API responses

## Data Storage Solutions
- **Database**: PostgreSQL configured through Drizzle ORM
- **Schema Design**: Three main entities - users, chat sessions, and chat messages
- **Temporary Storage**: In-memory storage class for development/testing with interface abstraction for production database integration
- **Session Tracking**: Active chat sessions with start/end times and message counts

## Authentication and Authorization
- **Current State**: Basic user structure defined in schema but authentication not yet implemented
- **Prepared Infrastructure**: User table with username/password fields ready for authentication integration

## External Dependencies
- **OpenAI API**: GPT-5 model integration for generating therapeutic responses with crisis detection capabilities
- **Neon Database**: PostgreSQL hosting service configured as the primary database provider
- **Tailwind CSS**: Utility-first CSS framework for responsive design
- **shadcn/ui**: Pre-built accessible component library built on Radix UI primitives
- **Development Tools**: Vite for fast development builds, ESBuild for production bundling

## Key Design Patterns
- **Repository Pattern**: Storage interface abstraction allows switching between in-memory and database implementations
- **WebSocket Message Handling**: Type-safe message schema using Zod for real-time communication validation
- **Component Composition**: Modular React components with clear separation of concerns
- **Crisis Detection**: Integrated safety features that can identify concerning messages and provide immediate resources
- **Responsive Design**: Mobile-first approach with adaptive layouts for different screen sizes