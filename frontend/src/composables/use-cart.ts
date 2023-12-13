import { Product } from '@/api';
import { useStorage } from '@vueuse/core';

export const cart = useStorage(
  'cart',
  {
    cart: [] as Product[],
    quantityMap: new Map<number, number>()
  },
  localStorage
);

/**
 * Retuns cart store
 */
export function useCart(): typeof cart {
  return cart;
}
