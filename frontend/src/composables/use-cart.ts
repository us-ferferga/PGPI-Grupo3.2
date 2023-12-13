import { Product } from '@/api';
import { Ref, ref } from 'vue';

export const cart = ref<Product[]>([]);
/**
 *
 */
export function useCart(): Ref<Product[]> {
  return cart;
}
