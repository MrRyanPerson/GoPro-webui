import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import adapter from '@sveltejs/adapter-node';
import { defineConfig } from 'vite';

export default defineConfig({ plugins: [
    tailwindcss(), 
    sveltekit({
        adapter: adapter(),
        compilerOptions: {
            experimental: {
                async: true
            }
        },
        experimental: {
            remoteFunctions: true
        }
    }
    )] 
});
