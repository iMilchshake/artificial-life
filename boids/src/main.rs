use std::f32::consts::PI;

use ggez::{
    event,
    glam::*,
    graphics::{self, Color},
    Context, GameError, GameResult,
};

use rand::prelude::*;

struct Boid {
    pos: Vec2,
    vel: f32,
    angle: f32,
}

fn random_vector(max_magnitude: f32, rng: &mut ThreadRng) -> Vec2 {
    let dist: f32 = rng.gen::<f32>() * max_magnitude;
    Vec2::from_angle(rng.gen::<f32>() * 2.0 * PI) * dist
}

impl Boid {
    fn spawn_boids(num: usize, pos: Vec2, spread: f32) -> Vec<Boid> {
        let mut boids = Vec::new();
        let mut rnd = rand::thread_rng();
        for _ in 0..num {
            let p = pos + random_vector(spread, &mut rnd);
            boids.push(Boid {
                pos: p,
                vel: 1.0,
                angle: rnd.gen::<f32>() * 360.0,
            });
        }
        return boids;
    }

    fn update(&mut self, _ctx: &mut Context) {
        self.pos += Vec2::from_angle(self.angle.to_radians()) * self.vel;
    }

    fn draw(&mut self, ctx: &mut Context, canvas: &mut graphics::Canvas) {
        // TODO: store mesh definitions in state??
        let circle = graphics::Mesh::new_circle(
            ctx,
            graphics::DrawMode::fill(),
            vec2(0., 0.),
            10.0,
            2.0,
            Color::WHITE,
        )
        .unwrap();

        canvas.draw(&circle, self.pos);
    }
}

struct GameState {
    boids: Vec<Boid>,
}

impl GameState {
    fn new(ctx: &mut Context) -> GameResult<GameState> {
        let boids = Boid::spawn_boids(20, vec2(300.0, 300.0), 50.0);

        Ok(GameState { boids })
    }
}

impl event::EventHandler<GameError> for GameState {
    fn update(&mut self, _ctx: &mut Context) -> GameResult {
        for boid in self.boids.iter_mut() {
            boid.update(_ctx);
        }

        Ok(())
    }

    fn draw(&mut self, ctx: &mut Context) -> GameResult {
        let mut canvas = graphics::Canvas::from_frame(ctx, graphics::Color::BLACK);
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
