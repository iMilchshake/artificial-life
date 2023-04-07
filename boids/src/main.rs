//! The simplest possible example that does something.
#![allow(clippy::unnecessary_wraps)]

use ggez::{
    event,
    glam::*,
    graphics::{self, Color},
    Context, GameError, GameResult,
};

struct Boid {
    pos: Vec2,
    vel: f32,
    angle: f32,
}

impl Boid {
    fn new() -> Boid {
        Boid {
            pos: vec2(100., 100.),
            vel: 0.,
            angle: 0.,
        }
    }

    fn update(&mut self, _ctx: &mut Context) {
        self.pos.x += 1.0;
    }

    fn draw(&mut self, ctx: &mut Context, canvas: &mut graphics::Canvas) {
        let circle = graphics::Mesh::new_circle(
            ctx,
            graphics::DrawMode::fill(),
            vec2(0., 0.),
            10.0,
            2.0,
            Color::WHITE,
        ).unwrap();

        canvas.draw(&circle, self.pos);
    }
}

struct GameState {
    pos_x: f32,
    circle: graphics::Mesh,
    boids: Vec<Boid>,
}

impl GameState {
    fn new(ctx: &mut Context) -> GameResult<GameState> {
        let boids = vec![Boid::new()];
        let circle = graphics::Mesh::new_circle(
            ctx,
            graphics::DrawMode::fill(),
            vec2(0., 0.),
            100.0,
            2.0,
            Color::WHITE,
        )?;

        Ok(GameState {
            pos_x: 0.0,
            circle,
            boids,
        })
    }
}

impl event::EventHandler<GameError> for GameState {
    fn update(&mut self, _ctx: &mut Context) -> GameResult {
        self.pos_x = self.pos_x % 800.0 + 1.0;
        for boid in self.boids.iter_mut() {
            boid.update(_ctx);
        }
        println!("{}", self.pos_x);

        Ok(())
    }

    fn draw(&mut self, ctx: &mut Context) -> GameResult {
        let mut canvas = graphics::Canvas::from_frame(ctx, graphics::Color::BLACK);
        canvas.draw(&self.circle, Vec2::new(self.pos_x, 380.0));
        for boid in self.boids.iter_mut() {
            boid.draw(ctx, &mut canvas);
        }
        canvas.finish(ctx)?;

        Ok(())
    }
}

pub fn main() -> GameResult {
    let cb = ggez::ContextBuilder::new("super_simple", "ggez");
    let (mut ctx, event_loop) = cb.build()?;
    let state = GameState::new(&mut ctx)?;
    event::run(ctx, event_loop, state)
}
